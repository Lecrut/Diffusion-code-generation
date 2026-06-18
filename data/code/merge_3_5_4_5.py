length_a = 150
length_b = 98
difference = length_a - length_b

if difference > 0:
    print(f'Length A is longer than Length B by {int(difference)} units')
elif difference < 0:
    print(f'Length B is longer than Length A by {-1 * int(difference)} units')
else:
    print('Both lengths are equal.')

if __name__ == '__main__':
    pass