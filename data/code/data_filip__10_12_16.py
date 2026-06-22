import io

class StringReverser:
    @staticmethod
    def reverse_words(text):
        if not text:
            return ""
        
        output = io.StringIO()
        length = len(text)
        i = 0
        
        while i < length:
            while i < length and text[i] == ' ':
                i += 1
            
            if i < length:
                start = i
                while i < length and text[i] != ' ':
                    i += 1
                if output.tell() > 0:
                    output.write(' ')
                output.write(text[start:i])
            
            while i < length and text[i] == ' ':
                i += 1
            
            if i < length:
                output.write(' ')
        
        result = output.getvalue()
        output.close()
        
        if not result:
            return ""
        
        words = result.split()
        reversed_words = words[::-1]
        
        final_output = io.StringIO()
        for idx, word in enumerate(reversed_words):
            if idx > 0:
                final_output.write(' ')
            final_output.write(word)
        
        return final_output.getvalue()

if __name__ == '__main__':
    sample_input = "  hello   world  this  is  a  test  "
    reverser = StringReverser()
    result = reverser.reverse_words(sample_input)
    print(result)