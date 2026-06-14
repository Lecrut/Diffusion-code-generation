def generate_pattern():
    line = "X"
    repeated_pattern = line * 10
    final_pattern = "\n".join([repeated_pattern] * 10)
    return final_pattern
if __name__ == '__main__':
    result = generate_pattern()
    print(result)