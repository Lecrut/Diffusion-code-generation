def reverse_word(word):
    def reverse_helper(index):
        if index < 0:
            return ""
        return word[index] + reverse_helper(index - 1)
    
    return reverse_helper(len(word) - 1)

if __name__ == '__main__':
    sample_word = "test"
    print(reverse_word(sample_word))