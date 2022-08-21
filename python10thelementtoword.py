words = {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
        50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
        90: 'Ninety', 100: 'Hundred'}

for number in range(1,101):
    if number in words:
        print(words[number])
    else:
        print(number)