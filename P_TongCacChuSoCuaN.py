n = int(input("Nhập số nguyên dương n : "))
total = 0

while n:
    total += n % 10
    n //= 10

print("Tổng các chữ số của n là : ", total)

