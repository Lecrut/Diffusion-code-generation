if __name__ == '__main__':
    numbers = [10, 5, 20, 8, 15]
    result = lambda nums: {'smallest': min(nums), 'largest': max(nums)}
    print(result(numbers))