id_user = None
input_data = None
result = None


def get_id_user(num_id):
    """Получение id пользователя"""
    global id_user
    id_user = num_id


def get_input_data(data):
    """Получение введенного пользователем примера"""
    global input_data
    input_data = data


def get_result(res):
    """Получение результата примера"""
    global result
    result = res


def save_log():
    """Запись данных в log"""
    with open('log_file.txt', 'a', encoding="utf-8") as f:
        f.writelines(f'ID user: {id_user}, Input: {input_data}, Result: {result}\n')