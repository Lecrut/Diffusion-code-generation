from functools import reduce
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers) if __name__ == '__main__' else list(reduce(lambda acc, x: (x < acc[0]) and ([x]+acc[:-1],)[-1] or acc, numbers))
if __name__ == '__main__':
    print(sorted_numbers)