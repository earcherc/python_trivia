def fib_gen(n):
    if n <= 0:
        return
    
    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


for num in fib_gen(10):
    print(num)

