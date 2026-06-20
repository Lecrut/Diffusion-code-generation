CONSONANTS = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def count_consonants(word):
    count = 0
    for char in word:
        if char.lower() in CONSONANTS:
            count += 1
    return count

if __name__ == '__main__':
    sample_word = "Programming"
    result = count_consonants(sample_word)
    print(result)