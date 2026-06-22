def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    print(average([1, 2, 3]))
    print(average([4]))
    print(average([]))