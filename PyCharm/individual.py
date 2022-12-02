cost_x, cost_y, cost_z = map(int, input("Введите цену за 1 кг конфет, печенья и яблок = ").split())
w_x, w_y, w_z = map(int, input("Введите сколько купили килограмм конфет, печенья и яблок = ").split())
sum = cost_x * w_x + cost_y * w_y + cost_z * w_z
print("Сумма всей покупки = ", sum)