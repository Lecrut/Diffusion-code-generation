def difference_length(length1, length2):
    return length1 - length2 if length1 > length2 else length2 - length1

if __name__ == '__main__':
    print(difference_length(10, 5))
    print(difference_length(5, 10))
    print(difference_length(10, 10))