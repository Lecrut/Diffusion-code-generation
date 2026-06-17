def repeat_phrase(n):
    if n == 0:
        return ""
    else:
        return repeat_phrase(n - 1) + "Repeat an action many times now"
if __name__ == '__main__':
    number = 3
    result = repeat_phrase(number)
    print(result)