import unicodedata

def count_consonants(text: str) -> int:
    vowels = set('aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛäëïöüÄËÏÖÜãẽĩõüÃẼĨÕÜåÅæÆøØαειουΑΕΙΟΥаяиеоуАЯИЕОУ')
    count = 0
    for char in text:
        if unicodedata.category(char).startswith('L'):
            if char.casefold() not in {v.casefold() for v in vowels}:
                count += 1
    return count
if __name__ == '__main__':
    sample_string = 'Hello World! This is a test with some Unicode characters: café, naïve, résumé.'
    result = count_consonants(sample_string)
    print(result)