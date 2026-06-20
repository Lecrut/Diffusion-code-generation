def partition_and_sort(int_list):
    odd = []
    even = []
    for num in int_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    odd.sort()
    even.sort()
    return (odd, even)
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    odd, even = partition_and_sort(sample_list)
    print(f'Odd numbers: {odd}')
    print(f'Even numbers: {even}')