def sort_three_numbers(x, y, z):
    if x > y:
        temp = x
        x = y
        y = temp
    if x > z:
        temp = x
        x = z
        z = temp
    if y > z:
        temp = y
        y = z
        z = temp
    return x, y, z

if __name__ == '__main__':
    sorted_numbers = sort_three_numbers(45, 12, 36)
    print(sorted_numbers)