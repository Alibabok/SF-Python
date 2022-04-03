per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
cont = int(input("Введите сумму, которую вы положите на год"))

deposit1 = cont/100*per_cent['ТКБ']
deposit2 = cont/100*per_cent['СКБ']
deposit3 = cont/100*per_cent['ВТБ']
deposit4 = cont/100*per_cent['СБЕР']

print("Ваш депозит за год составит: ТКБ -", deposit1,
                                    "СКБ - ", deposit2,
                                        "ВТБ - ", deposit3,
                                            "СБЕР - ", deposit4)

deposit_list = [deposit1, deposit2, deposit3, deposit4]
max_deposit = max(deposit_list)

print("Максимальная сумма, которую вы можете заработать — ", max_deposit)
