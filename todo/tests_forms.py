from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.'
        )

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        # The fields variable is a list of all the fields that are in the form.
        # Check that the fields in the form are the same as we expect.
        self.assertEqual(form.Meta.fields, ['name', 'done'])
