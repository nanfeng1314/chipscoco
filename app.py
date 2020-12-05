def shopping():
    prompt = "你好，欢迎使用薯条橙子在线购物系统chipscoco，\n" \
             "输入<>中对应的指令来使用购物系统\n" \
             "<1>:查看所有商品" \
             "<2>:对商品按售价进行排序（asc表示升序、desc表示降序）\n" \
             "<3>:添加商品到购物车\n" \
             "<4>:查看购物车\n" \
             "<5>:删除购物车指定商品\n" \
             "<6>:下单结账\n" \
             "<0>:退出系统"
    commands = {
        1:show_all_goods,
        2:sort_goods,
        3:add_goods,
        4:show_shopping_cart,
    }
    while Ture:
        print(prompt)
        command = int(input("输入指令：__\b\b"))
        if command in commands:
            commands[command](chipscoco)
        elif command == 0:
            break
        else:
            print("你输入了非法指令")
        input("按下键盘任意键，继续使用系统......")

if __name__ == "__main__":
    shopping()