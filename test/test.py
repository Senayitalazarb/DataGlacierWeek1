from app import create_name
def my_first_test():
    name_sport = create_name('Senayit Berhane','Basketball')

    assert name_sport == 'My name is Senayit Berhane and my favorite sport is Basketball'