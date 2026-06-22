def interleave_strings(str1: str, str2: str) -> str:
    if not all(isinstance(s, str) for s in (str1, str2)):
        raise ValueError("Both inputs must be strings.")
    return ''.join([str1[i] + str2[i] if i < min(len(str1), len(str2)) else '' for i in range(max(len(str1), len(str2)))]) + str1[min(len(str1), len(str2)):] + str2[min(len(str1), len(str2)):]

if __name__ == '__main__':
    result = interleave_strings('hello', 'world')
    print(result)