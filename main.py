card_number = input("Kart numaranızı giriniz: ")

def luhn(card_number):
    if len(card_number) == 16:
        check_list = []
        for i in range(0,16):
            check_list.append(int(card_number[i]))
        for n in range(0,16):
            if n % 2 == 0:
                if check_list[n]*2 > 9:
                    n_new = str(check_list[n]*2)
                    n_first = n_new[0]
                    n_second = n_new[1]
                    n_total = int(n_first) + int(n_second)
                    check_list[n] = n_total
                else:
                    check_list[n] = check_list[n]*2
        numbers_total = 0
        for nk in check_list:
            numbers_total += nk
        if numbers_total % 10 != 0:
            return "Geçersiz kart numarası"
        elif str(numbers_total).endswith("0"):

            return "kart numarası geçerli"
        else:
            return "Geçersiz kart numarası"
    else:
        return "Geçersiz kart numarası"

print(luhn(card_number))
