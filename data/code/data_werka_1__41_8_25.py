def case_swap(text):
    LOWERCASE = 'lower'
    UPPERCASE = 'upper'
    TITLECASE = 'title'
    
    return {
        LOWERCASE: text.lower(),
        UPPERCASE: text.upper(),
        TITLECASE: text.title()
    }

if __name__ == '__main__':
    SAMPLE_TEXT = "Hello World"
    result = case_swap(SAMPLE_TEXT)
    print(result)