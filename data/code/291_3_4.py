def compare_lengths(km1, m1, km2, m2):
    total_m1 = km1 * 1000 + m1
    total_m2 = km2 * 1000 + m2
    if total_m1 == total_m2:
        return 'Equal'
    elif total_m1 > total_m2:
        return 'First length is longer'
    else:
        return 'Second length is longer'
if __name__ == '__main__':
    print(compare_lengths(5, 300, 4, 900))
    print(compare_lengths(3, 150, 3, 150))
    print(compare_lengths(2, 750, 3, 250))