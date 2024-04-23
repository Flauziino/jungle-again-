from django import forms
from visitantes.models import Visitante


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento",
            "numero_casa", "placa_veiculo",
        ]
        error_messages = {
            "nome_completo": {
                "required": "O nome completo do visitante é obrigatório para o registro."  # noqa: E501
            },
            "cpf": {
                "required": "O CPF do visitante é obrigatório para o registro."
            },
            "data_nascimento": {
                "required": "A data de nascimento do visitante é obrigatório para o registro",  # noqa: E501
                "invalid": "Por favor, infome um formato válido para a data de nascimento. Ex:(DD/MM/AAAA)"  # noqa: E501
            },
            "numero_casa": {
                "required": "Por favor, informe o número da casa a ser visitada."  # noqa: E501
            }
        }


class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel"
        ]
        error_messages = {
            "morador_responsavel": {
                "required": "Por favor, informe o nome do morador responsável"
            }
        }
