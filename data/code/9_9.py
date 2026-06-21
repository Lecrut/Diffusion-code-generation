class CurrencyConversionError(Exception):
    def __init__(self, message, details):
        super().__init__(message)
        self.details = details

class InvalidCurrencyCodeError(CurrencyConversionError):
    def __init__(self, from_currency, to_currency):
        message = f"Invalid currency code: {from_currency} or {to_currency}"
        details = {"from": from_currency, "to": to_currency}
        super().__init__(message, details)

class InsufficientFundsError(CurrencyConversionError):
    def __init__(self, amount, required_balance):
        message = f"Insufficient funds: {amount} requested but only {required_balance} available"
        details = {"requested": amount, "available": required_balance}
        super().__init__(message, details)

class ZeroAmountError(CurrencyConversionError):
    def __init__(self, amount):
        message = f"Conversion amount cannot be zero or negative: {amount}"
        details = {"amount": amount}
        super().__init__(message, details)

EXCHANGE_RATES = {
    ("USD", "EUR"): 0.85,
    ("USD", "GBP"): 0.75,
    ("EUR", "USD"): 1.18,
    ("GBP", "USD"): 1.33,
    ("EUR", "GBP"): 0.88,
    ("GBP", "EUR"): 1.14,
}

WALLETS = {
    "USD": 10000.0,
    "EUR": 5000.0,
    "GBP": 7500.0,
}

def get_rate(from_currency, to_currency):
    pair = (from_currency, to_currency)
    if pair in EXCHANGE_RATES:
        return EXCHANGE_RATES[pair]
    reverse_pair = (to_currency, from_currency)
    if reverse_pair in EXCHANGE_RATES:
        return 1.0 / EXCHANGE_RATES[reverse_pair]
    valid_codes = set()
    for p in EXCHANGE_RATES:
        valid_codes.add(p[0])
        valid_codes.add(p[1])
    if from_currency not in valid_codes or to_currency not in valid_codes:
        raise InvalidCurrencyCodeError(from_currency, to_currency)
    raise CurrencyConversionError("Rate not found", {"from": from_currency, "to": to_currency})

def convert_currency(from_currency, to_currency, amount):
    if amount <= 0:
        raise ZeroAmountError(amount)
    if from_currency not in WALLETS:
        raise InvalidCurrencyCodeError(from_currency, to_currency)
    if to_currency not in WALLETS:
        raise InvalidCurrencyCodeError(from_currency, to_currency)
    current_balance = WALLETS.get(from_currency, 0.0)
    if amount > current_balance:
        raise InsufficientFundsError(amount, current_balance)
    rate = get_rate(from_currency, to_currency)
    converted_amount = amount * rate
    return converted_amount

if __name__ == '__main__':
    sample_from = "USD"
    sample_to = "EUR"
    sample_amount = 1000.0
    try:
        result = convert_currency(sample_from, sample_to, sample_amount)
        print(result)
    except CurrencyConversionError as e:
        print(e)