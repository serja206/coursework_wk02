"""
RECORD CHECK  -  my version
===========================

Name  :  Yousef
Lane  :  Cyber
Date  : 10/01/2026

Run it:   w02_miniproj.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# asking for 3 things, ip does not need converting because it's text

label = input("Source IP     : ")
value = float(input("Failed logins     : "))
limit = float(input("Total attempts     : "))

difference = value - limit  # formula to find the difference
percent = (value / limit) * 100  # formula to find the percentage

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"  Failed logins : {value:>10.2f}")
print(f"  Total attempts: {limit:>10.2f}")
print(f"  Remaining     : {difference:>10.2f}")
print(f"  Percent       : {percent:>10.2f} %")
print(f"  Status        : {status:>10}")
print("=" * 34)
