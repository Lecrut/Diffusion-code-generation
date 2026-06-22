CONSONANTS = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

def count_consonants(word):
    count = 0
    for char in word:
        if char in CONSONANTS:
            count += 1
    return count

if __name__ == '__main__':
    sample_words = ['hello', 'python', 'aeiou', 'xyz', '']
    for word in sample_words:
        result = count_consonants(word)
        print(result)