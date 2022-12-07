import re

n = input('Enter Mobile number :')
r = re.fullmatch("^(\+)?(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$",n)
if r != None:
    print('Valid Number')
else:
    print('Not a valid number')

# ● 2124567890 (run)
# ● 212-456-7890 (run)
# ● (212)456-7890 (run)
# ● (212)-456-7890 (run)
# ● 212.456.7890 (run)
# ● 212 456 7890 (run)
# ● +12124567890 (run)
# ● +12124567890 (run)
# ● +1 212.456.7890 (run)
# ● +212-456-7890 (run)
# ● 1-212-456-7890 (run)