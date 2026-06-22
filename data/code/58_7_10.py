def count_even_in_range(start, stop):
    count = 0
    if stop < start:
        return 0
    for num in range(start, stop):
        if num % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    result = count_even_in_range(-5, 5)
    print(result)