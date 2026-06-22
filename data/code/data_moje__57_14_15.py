fib = [0]
fib.extend([fib.append(fib[-1] + fib[-2]) or fib[-1] for _ in range(14)])
if __name__ == '__main__':
    print(fib[:15])