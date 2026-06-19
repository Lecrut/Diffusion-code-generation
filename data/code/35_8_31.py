def count_vowels(text):
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_text1 = "Alibaba Cloud"
    sample_text2 = "OpenAI GPT-4"
    sample_text3 = "Python Programming"
    sample_text4 = "Vowels Counting"
    
    count1 = count_vowels(sample_text1)
    count2 = count_vowels(sample_text2)
    count3 = count_vowels(sample_text3)
    count4 = count_vowels(sample_text4)
    
    print(count1)
    print(count2)
    print(count3)
    print(count4)