
# iterative approach:
def fibonacci(num):
    a, b = 0, 1

    for i in range(num):
        a, b = b, a + b

    return a


# recursive approach without count the number of stack frames:
def fib(num):
    if num < 2:
        return num
    return fib(num-1) + fib(num-2)



# dynamic programing approach with strack:
'''
this approach:
    1. Add caching (memoization)
'''
def fib(num):
    memo = {0:0, 1:1}

    def f(x):
        if x in memo:
            return memo[x]
        memo[x] = f(x-1) + f(x-2)
        return memo[x]
    
    return f(num)


'''
to also count the number of stack frames , this approach:
    1. memoization (DP)
    2. call counting (stack frames / function calls)
'''
def fib(num):
    memo = {0:0, 1:1}
    count = {"calls": 0}

    def f(x):
        count["calls"] += 1
        if x in memo:
            return memo[x]
        memo[x] = f(x-1) + f(x-2)
        return memo[x]
    
    return f(num), count["calls"]






# if (require.main === module) {
# // add your own tests in here
# console.log("Expecting: 0");
# console.log("=>", fibonacci(0));

# console.log("");

# console.log("Expecting: 1");
# console.log("=>", fibonacci(2));

# console.log("");

# console.log("Expecting: 55");
# console.log("=>", fibonacci(10));
# }

# module.exports = fibonacci;

# // Please add your pseudocode to this file
# // And a written explanation of your solution