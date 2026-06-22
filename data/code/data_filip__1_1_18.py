import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov|mil|io|co|us|uk|ca|au|de|fr|jp|cn|in|ru|br|it|es|nl|se|no|dk|fi|pl|cz|hu|ro|bg|hr|sk|si|lt|lv|ee|is|ie|pt|gr|tr|il|ae|sa|qa|kw|bh|om|jo|lb|eg|ma|tn|dz|ly|ne|sd|et|ke|ng|gh|ug|tz|zw|zm|bw|na|mz|mz|ao|cg|cd|cf|td|cm|ga|gq|st|cv|gw|sn|gm|ml|bf|ci|lr|sl|gn|tg|bj|mu|mg|re|yt|nc|pf|wf|su|tk|to|vu|fj|pg|sb|kp|vn|mm|la|kh|th|my|sg|id|ph|tw|hk|mo|cn|tw|jp|kr|mn|ru|by|ua|md|ge|am|az|ir|iq|sy|ye|ly|ma|dz|tn|eg|sa|kw|qa|bh|om|ae|il|jo|lb|sy|iq|ir|af|pk|in|bd|lk|np|bt|mv|mm|kh|la|vn|th|my|sg|id|ph|tw|hk|mo|cn|tw|jp|kr|mn|ru|by|ua|md|ge|am|az|ir|iq|sy|ye|ly|ma|dz|tn|eg|sa|kw|qa|bh|om|ae|il|jo|lb|sy|iq|ir|af|pk|in|bd|lk|np|bt|mv|mm|kh|la|vn|th|my|sg|id|ph|tw|hk|mo|cn|tw|jp|kr|mn)$'
    return bool(re.match(pattern, email))

if __name__ == '__main__':
    test_emails = [
        "user@example.com",
        "invalid.email@",
        "user@domain",
        "valid.email@company.org",
        "@missinglocal.com",
        "user.name+tag@domain.co",
        "bad@@double.com"
    ]
    results = [validate_email(email) for email in test_emails]
    print(results)