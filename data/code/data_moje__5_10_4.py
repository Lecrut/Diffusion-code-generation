def length_difference(length1, length2):
    return length1 - length2 if length1 >= length2 else length2 - length1

if __name__ == '__main__':
    result = length_difference(10, 5)
    print(result)