def concatenate_and_format(str1, str2):
    combined = str1 + str2
    return f"Result: {combined}"

if __name__ == '__main__':
    part1 = "Greetings from "
    part2 = "Alibaba Cloud!"
    formatted_result = concatenate_and_format(part1, part2)
    print(formatted_result)