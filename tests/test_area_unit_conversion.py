import pytest
import area_unit_conversion
from area_unit_conversion import __version__


def test_version():
    assert __version__ == '1.0'


class TestConvert:

    @pytest.mark.parametrize("input_value, expected_value", [
        ("km2", 1),
        ("m2", 1000000),
        ("mi2", 0.3861003861003861),
        ("yd2", 1195984.5555359856),
        ("ft2", 10763860.99982387),
        ("in2", 1549995983.9746373),
        ("ha", 100.0),
        ("ac", 247.10424701156725),
    ])
    def test_km2(self, input_value, expected_value):
        assert area_unit_conversion.convert('km2', input_value, 1) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("km2", 0.000001),
        ("m2", 1),
        ("mi2", 0.0000003861003861003861),
        ("yd2", 1.1959845555359856),
        ("ft2", 10.76386099982387),
        ("in2", 1549.9959839746373),
        ("ha", 0.0001),
        ("ac", 0.00024710424701156723),
    ])
    def test_m2(self, input_value, expected_value):
        assert area_unit_conversion.convert('m2', input_value, 1) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("km2", 2.59),
        ("m2", 2590000.0),
        ("mi2", 1),
        ("yd2", 3097599.9988382026),
        ("ft2", 27878399.98954382),
        ("in2", 4014489598.494311),
        ("ha", 259.0),
        ("ac", 639.9999997599592),
    ])
    def test_mi2(self, input_value, expected_value):
        assert area_unit_conversion.convert('mi2', input_value, 1) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("km2", 0.00000083613119866071),
        ("m2", 0.83613119866071),
        ("mi2", 0.00000032283057863347875),
        ("yd2", 1.0),
        ("ft2", 9.0),
        ("in2", 1296.0),
        ("ha", 0.000083613119866071),
        ("ac", 0.00020661157024793388),
    ])
    def test_yd2(self, input_value, expected_value):
        assert area_unit_conversion.convert('yd2', input_value, 1) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("km2", 0.00000009290346651785667),
        ("m2", 0.09290346651785666),
        ("mi2", 0.00000003587006429260875),
        ("yd2", 0.11111111111111112),
        ("ft2", 1.0),
        ("in2", 144.0),
        ("ha", 0.000009290346651785667),
        ("ac", 0.000022956841138659323),
    ])
    def test_ft2(self, input_value, expected_value):
        assert area_unit_conversion.convert('ft2', input_value, 1) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("km2", 0.0000000006451629619295601),
        ("m2", 0.0006451629619295601),
        ("mi2", 0.00000000024909766869867187),
        ("yd2", 0.0007716049382716049),
        ("ft2", 0.006944444444444444),
        ("in2", 1.0),
        ("ha", 0.000000064516296192956),
        ("ac", 0.00000015942250790735638),
    ])
    def test_in2(self, input_value, expected_value):
        assert area_unit_conversion.convert('in2', input_value, 1) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("km2", 0.01),
        ("m2", 10000.0),
        ("mi2", 0.003861003861003861),
        ("yd2", 11959.845555359856),
        ("ft2", 107638.6099982387),
        ("in2", 15499959.839746373),
        ("ha", 1.0),
        ("ac", 2.4710424701156724),
    ])
    def test_ha(self, input_value, expected_value):
        assert area_unit_conversion.convert('ha', input_value, 1) == expected_value

    @pytest.mark.parametrize("input_value, expected_value", [
        ("km2", 0.004046875001517836),
        ("m2", 4046.875001517836),
        ("mi2", 0.0015625000005860372),
        ("yd2", 4840.0),
        ("ft2", 43560.0),
        ("in2", 6272640.0),
        ("ha", 0.4046875001517836),
        ("ac", 1.0),
    ])
    def test_ac(self, input_value, expected_value):
        assert area_unit_conversion.convert('ac', input_value, 1) == expected_value
