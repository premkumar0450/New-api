from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def  test_create_user_with_email_successful(self):

        email = 'name@email.com'
        password = 'Testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):

        email= 'name@EMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(none, 'test123')


