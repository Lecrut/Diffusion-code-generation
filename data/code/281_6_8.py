def sum_of_nine_integers():
    return sum(n for n in range(1, 10))

if __name__ == '__main__':
    result = sum_of_nine_integers()
    print(result)