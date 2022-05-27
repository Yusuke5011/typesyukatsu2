def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
    low = 0
    high = len(sorted_array) - 1
    #配列の長さを取得する
    while low <= high:
        mid = (low + high) // 2
       #中間の値が取れるまで、試行を繰り返す
        if sorted_array[mid] == target_number:
            print(sorted_array.index(target_number))
            #探索した値と目標値が一致したら、目標値のindexを表示する
            return
        elif sorted_array[mid] < target_number:
            low = mid + 1
            #配列の左側から順に、値に近づける
        else:
            high = mid - 1
            #配列の右側から順に、値に近づける
    return
    
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
