import re

def split_preserving_quotes(text):
    if not text:
        return []
    pattern = r'''('[^']*'|" [^"]*" | [^,])+ '''
    pattern = r'''('[^']*'|" [^"]*" | [^,])+ '''
    pattern = r'''(" [^"]*" | ' [^']*' | [^,])+'''
    pattern = r'''(" [^"]*" | ' [^']*' | [^,])+'''
    pattern = r'''(" [^"]*" | '[^']*' | [^,])+'''
    pattern = r'''(" [^"]*" | '[^']*' | [^,])+'''
    pattern = r'''("[^"]*"|'[^']*'|[^,])+'''
    matches = re.findall(r'"[^"]*"|\'[^\']*\'|[^,]+', text)
    return [m.strip() for m in matches]

if __name__ == '__main__':
    sample_input = 'apple, "red, green", banana, \'blue, yellow\', cherry'
    result = split_preserving_quotes(sample_input)
    print(result)