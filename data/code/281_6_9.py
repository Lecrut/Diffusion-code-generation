def sum_of_nine_integers():
    return sum(x for x in range(9))

if __name__ == '__main__':
    result = sum_of_nine_integers()
    print(result)