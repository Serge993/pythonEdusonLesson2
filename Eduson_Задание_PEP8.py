first_koeficent = int(input('a = ', ))
second_koeficent = int(input('b = ', ))
third_koeficent = int(input('c = ', ))


# решение по сокращенной формуле, т.к. второй коэфицент - четное
if first_koeficent != 0 and second_koeficent % 2 == 0 and third_koeficent != 0:
    k = second_koeficent / 2
    discriminant_1 = k ** 2 - first_koeficent * third_koeficent
    root_first = (-k + discriminant_1 ** 0.5) / first_koeficent
    root_second = (-k - discriminant_1 ** 0.5) / first_koeficent

    print('так как второй коэффициент - четное число, решаем по сокращенной формуле')
    print(f'первый корень = {root_first}')
    print(f'второй корень = {root_second}')


# решение полного уравнения
if first_koeficent != 0 and second_koeficent % 2 != 0 and third_koeficent != 0:
    discriminant_ = second_koeficent ** 2 - 4 * first_koeficent * third_koeficent
    if discriminant_ > 0:
        root = (-second_koeficent + discriminant_ ** 0.5) / (2 * first_koeficent)
        print(f'дискриминант равен: {discriminant_}')
        print(f'первый корень равен: {round(root_first, 2)}')
        root_second = (-second_koeficent - discriminant_ ** 0.5) / (2 * first_koeficent)
        print(f'второй корень равен: {round(root_second, 2)}')  
    elif discriminant_ < 0:
        print(f'так как дискриминант меньше нуля и равен: {discriminant_}')
        print('действительных корней нет') 
    else:
        root = -second_koeficent / (2 * first_koeficent)
        print(f'уравнение имеет один корень: {root}')
        if first_koeficent != 0 and third_koeficent != 0 and second_koeficent == 0:
            if (- third_koeficent / first_koeficent) >= 0:
                root_first = (-third_koeficent / first_koeficent) ** 0.5
                print(f'первый корень равен: {root_first}')
                root_second = (-1) * ((-third_koeficent / first_koeficent) ** 0.5)
                print(f'второй корень равен: {root_second}')
        if (- third_koeficent / first_koeficent) < 0:
            print(f' -c / peremennaya1 = : {-third_koeficent / first_koeficent},'
                  f' т.е. < 0, поэтому действительных корней нет'
                  )

        # решение уравнения при с = 0
if first_koeficent != 0 and third_koeficent== 0 and second_koeficent != 0:
    print(f'корень уравнения равен либо нулю, либо {-second_koeficent / first_koeficent}')

    # решение уравнения при b = 0 и c = 0
if first_koeficent != 0 and second_koeficent== 0 and third_koeficent == 0:
    print(f'корни уравнения равны нулю,')