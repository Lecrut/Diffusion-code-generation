if __name__ == '__main__':
    numbers = [15, 3, 8, 22, 1]
    result = lambda nums: {'smallest': min(nums), 'largest': max(nums)}
    print(result(numbers))