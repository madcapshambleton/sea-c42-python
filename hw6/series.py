def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x, y):
    if x == 0 and y == 1:
        return fibonacci(n)
    if x == 2 and y == 1:
        return lucas(n)

print sum_series(3, x=2, y=1)
print sum_series(3)
