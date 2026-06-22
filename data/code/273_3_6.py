def reverse_and_repeat(instructions, n):
    if not instructions or n <= 0:
        return []
    
    reversed_instructions = instructions[::-1]
    result = [eval(instruction) for instruction in reversed_instructions[:n]]
    return result

if __name__ == '__main__':
    sample_instructions = ["print('Hello')", "print('World')"]
    count = 2
    result = reverse_and_repeat(sample_instructions, count)
    print(result)