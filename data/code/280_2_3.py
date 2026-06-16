def repeat_phrase(n, phrase):
    if n == 0:
        return ""
    else:
        return repeat_phrase(n - 1, phrase) + " " + phrase
if __name__ == '__main__':
    count = 5
    text = "Repeat an action many times now"
    result = repeat_phrase(count, text)
    print(result)