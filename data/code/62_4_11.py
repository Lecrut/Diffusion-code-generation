def divisors_of_60():
    return [i for i in range(1, 61) if 60 % i == 0]

if __name__ == '__main__':
    print(divisors_of_60())