counter = 0
while counter < 100:
    print(f'Action performed {counter + 1} times')
    counter += 1
if __name__ == '__main__':
    number_of_repeats = 5
    phrase_to_repeat = 'Repeat an action many times now'

    def repeat_phrase(n, phrase):
        result = ''
        while n > 0:
            result += phrase + ' '
            n -= 1
        return result.strip()
    repeated_result = repeat_phrase(number_of_repeats, phrase_to_repeat)
    print(repeated_result)