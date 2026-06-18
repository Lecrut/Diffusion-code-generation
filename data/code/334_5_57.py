def combined_generator(s1: str, s2: str) -> str:
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        yield f"{s1[i]}{s2[j]}"
        i += 1
        j += 1
def main():
    s1_str = "Hello"
    s2_str = "World"
    result_generator = combined_generator(s1_str, s2_str)
    output_parts = []
    for char_pair in result_generator:
        output_parts.append(char_pair)
    print("".join(output_parts))
if __name__ == '__main__':
    main()