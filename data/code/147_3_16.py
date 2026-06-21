numbers = [3.5, 1.2, 4.8, 2.9]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

if __name__ == '__main__':
    sample_list = [5.6, 3.7, 2.1, 4.3]
    if all(isinstance(x, float) for x in sample_list):
        result = sorted(sample_list, reverse=True)
        print(result)