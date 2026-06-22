import sys

def strip_list_strings(strings):
    if not strings:
        return []
    return list(map(str.strip, strings))

if __name__ == '__main__':
    sample_data = ["  hello  ", "  world  ", "  python  "]
    result = strip_list_strings(sample_data)
    print(result)