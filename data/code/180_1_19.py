WORDS_SET = set("This is a sample text about python programming.".split())

def word_present(target_word):
    return target_word in WORDS_SET

if __name__ == '__main__':
    target1 = "python"
    print(f"'{target1}' present: {word_present(target1)}")
    target2 = "java"
    print(f"'{target2}' present: {word_present(target2)}")
    target3 = "missing"
    print(f"'{target3}' present: {word_present(target3)}")