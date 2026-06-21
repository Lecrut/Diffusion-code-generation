def largest_of_three(first: int, second: int, third: int) -> int:
    result = first
    if second > result:
        result = second
    if third > result:
        result = third
    return result

if __name__ == '__main__':
    val_1 = 42
    val_2 = 99
    val_3 = 15
    print(largest_of_three(val_1, val_2, val_3))