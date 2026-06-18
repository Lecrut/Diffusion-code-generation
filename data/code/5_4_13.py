length_a = 150
length_b = 98

if length_a > length_b:
    difference = length_a - length_b
    print(f'Length A is longer than Length B by {difference} units')
elif length_b > length_a:
    difference = length_b - length_a
    print(f'Length B is longer than Length A by {difference} units')
else:
    print('Both lengths are equal.')

if __name__ == '__main__':
    pass
