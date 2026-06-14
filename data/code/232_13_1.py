import sys
if __name__ == '__main__':
    limit = 30
    for i in range(limit + 1):
        power_of_two = 1 << i
        print(power_of_two)