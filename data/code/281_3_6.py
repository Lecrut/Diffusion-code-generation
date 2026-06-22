def sum_of_six_numbers(x, y, z, w, v, u):
    total = x + y + z + w + v + u
    return total

if __name__ == '__main__':
    sample_values = (15, 25, 35, 45, 55, 65)
    result = sum_of_six_numbers(*sample_values)
    print(result)