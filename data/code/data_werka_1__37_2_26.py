MAX_STRING_LENGTH = 1024

def concatenate(str1, str2):
    if len(str1) > MAX_STRING_LENGTH or len(str2) > MAX_STRING_LENGTH:
        raise ValueError("String length exceeds maximum allowed")
    return str1 + str2

if __name__ == '__main__':
    part1 = "Greetings from "
    part2 = "Alibaba Cloud!"
    combined_message = concatenate(part1, part2)
    print(combined_message)