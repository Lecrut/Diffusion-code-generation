def compress(s):
    if not s: return ''
    result, count, char = '', 0, None
    for c in s:
        if c == char: count += 1
        else: result += (char + str(count)) if count else ''; char, count = c, 1
    return result + (char + str(count)) if count else result

if __name__ == '__main__':
    print(compress('bbbaaa'))