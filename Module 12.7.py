per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input())
deposit = []
for key in per_cent:
    deposit.append(money / 100 * per_cent[key])
print("Максимальная сумма, которую вы можете заработать —", max(deposit))
