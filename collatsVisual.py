import matplotlib.pyplot as plt

def collatz(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
        yield n, steps

def visualize_collatz():
    n = int(input("Enter a starting value for the Collatz conjecture: "))

    xs = []
    ys = []
    for i, (num, step) in enumerate(collatz(n)):
        xs.append(i)
        ys.append(num)

    plt.plot(xs, ys)
    plt.show()

visualize_collatz()
