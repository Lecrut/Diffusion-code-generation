def sum_three_numbers(x: float, y: float, z: float) -> float:
    return x + y + z

if __name__ == '__main__':
    sample1 = 4.5
    sample2 = 5.5
    sample3 = 6.0
    
    result = sum_three_numbers(sample1, sample2, sample3)
    print(f"The sum of {sample1}, {sample2}, and {sample3} is: {result}")