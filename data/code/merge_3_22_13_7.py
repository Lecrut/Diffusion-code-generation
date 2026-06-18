result = True if num % 2 else False
if __name__ == '__main__':
    result1 = result if (num := -5) else None
    print(result, "is", end="")
    if not isinstance(num, int): raise TypeError("Number must be an integer.")
    sample_nums = [-4, 37]
    for n in sample_nums: num = n; out_result = result; assert (out_result == bool(n % 2))